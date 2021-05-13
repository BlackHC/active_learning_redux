store = {}
store['timestamp']=1620257845
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=6']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=6
store['worker_id']=6
store['num_workers']=40
store['config']={'seed': 7, 'acquisition_size': 20, 'max_training_set': 450, 'num_pool_samples': 50, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.218398332595825})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.3073229789733887})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.3925657272338867})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.694021224975586})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6709, 'crossentropy': 2.0320759765625}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 43297], ['id', 40977], ['id', 27418], ['id', 34770], ['id', 50284], ['ood', 38970], ['id', 47983], ['id', 27469], ['id', 10797], ['id', 18820], ['id', 19757], ['id', 10088], ['id', 42952], ['id', 25818], ['id', 57324], ['id', 8046], ['id', 48010], ['id', 48847], ['id', 24108], ['id', 29847]], 'labels': [3, 9, 8, 8, 4, 6, 5, 8, 8, 9, 9, 9, 4, 0, 8, 0, 7, 5, 8, 9], 'scores': [0.5985549688339233, 0.7560688853263855, 0.871379554271698, 0.7169205546379089, 0.9163534045219421, 0.462963342666626, 0.864611029624939, 0.8560456037521362, 0.7698849439620972, 0.8726372122764587, 0.8138593435287476, 0.8662956953048706, 0.8614045977592468, 0.832839846611023, 1.0683742761611938, 0.7646240592002869, 1.0822689533233643, 0.7729105949401855, 0.9102038145065308, 0.7637807726860046]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.5278806686401367})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.7065544128417969})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.975284457206726})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.8842827081680298})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7467, 'crossentropy': 1.23971171875}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 43967], ['id', 17715], ['id', 1096], ['id', 2856], ['id', 24541], ['id', 56164], ['id', 27629], ['id', 635], ['id', 35916], ['id', 45055], ['ood', 11355], ['id', 43373], ['id', 53844], ['id', 53939], ['id', 43213], ['id', 57285], ['id', 48423], ['id', 24716], ['id', 22537], ['id', 44249]], 'labels': [3, 3, 2, 4, 0, 3, 1, 5, 8, 2, 8, 3, 5, 1, 7, 7, 2, 5, 4, 3], 'scores': [0.4749841094017029, 0.6431593298912048, 0.5111263394355774, 0.6619518399238586, 0.48780280351638794, 0.6562880277633667, 0.6178414821624756, 0.5673668384552002, 0.629404604434967, 0.6684970855712891, 0.22827839851379395, 0.575590968132019, 0.506149411201477, 0.5505164861679077, 0.7054406404495239, 0.6585365533828735, 0.5100184082984924, 0.7708159685134888, 0.5040280222892761, 0.556722104549408]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.1925280094146729})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.2733981609344482})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.2795404195785522})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.4879348278045654})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.815, 'crossentropy': 1.00960126953125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 46215], ['id', 30864], ['id', 51620], ['id', 48997], ['id', 1245], ['id', 58771], ['id', 5137], ['id', 37905], ['id', 18803], ['id', 55897], ['id', 36660], ['id', 8328], ['id', 27899], ['id', 46715], ['id', 20587], ['id', 40775], ['id', 27793], ['id', 14828], ['id', 16298], ['id', 55638]], 'labels': [7, 5, 6, 8, 5, 2, 9, 6, 2, 6, 6, 6, 3, 6, 3, 6, 1, 5, 2, 6], 'scores': [0.41105031967163086, 0.49313944578170776, 0.6758924126625061, 0.5557293891906738, 0.476881206035614, 0.47549837827682495, 0.620793342590332, 0.45515137910842896, 0.558506965637207, 0.6692022681236267, 0.6090641021728516, 0.5144668817520142, 0.689263105392456, 0.6140197515487671, 0.516054630279541, 0.631642758846283, 0.6833235621452332, 0.5961686372756958, 0.48283809423446655, 0.5536757707595825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8923159837722778})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8912917375564575})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.996853232383728})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9585654735565186})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9971259832382202})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8763, 'crossentropy': 0.77413916015625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 20162], ['id', 21606], ['ood', 45935], ['id', 42201], ['id', 5250], ['id', 44090], ['id', 54100], ['id', 57601], ['id', 25478], ['id', 15750], ['id', 15715], ['id', 28880], ['id', 37880], ['id', 41488], ['id', 11534], ['id', 1058], ['id', 22593], ['id', 17052], ['id', 4328], ['id', 41911]], 'labels': [7, 3, 5, 3, 2, 2, 7, 0, 9, 7, 2, 7, 2, 6, 7, 2, 7, 2, 3, 2], 'scores': [0.7549617290496826, 0.9001893997192383, 0.5287427306175232, 0.7993289232254028, 0.9310353398323059, 0.7784059047698975, 0.8607628345489502, 0.6383876204490662, 0.5264397859573364, 0.7904563546180725, 0.7262381315231323, 0.8351417779922485, 0.6592033505439758, 0.6900585293769836, 0.6237479150295258, 0.5936106443405151, 0.8564910888671875, 0.9071520566940308, 0.7893729209899902, 0.963585376739502]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8160152435302734})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7099745273590088})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.734361469745636})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7919864654541016})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7865236401557922})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8919, 'crossentropy': 0.64474873046875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 51890], ['id', 39593], ['id', 7919], ['id', 1402], ['id', 23790], ['id', 749], ['id', 37275], ['id', 21353], ['id', 32892], ['id', 17952], ['id', 23824], ['id', 8234], ['id', 38613], ['id', 27406], ['id', 50459], ['id', 42249], ['id', 54986], ['id', 40677], ['id', 12463], ['id', 46502]], 'labels': [3, 9, 4, 5, 6, 4, 5, 0, 1, 8, 5, 8, 8, 7, 8, 4, 8, 4, 3, 8], 'scores': [0.6246928572654724, 0.8255735039710999, 0.6204168200492859, 0.6439211964607239, 0.6710289716720581, 0.6464046239852905, 0.5912941694259644, 0.6757128238677979, 0.7667620778083801, 0.5264780521392822, 0.6539534330368042, 0.8366673588752747, 0.62403804063797, 0.7485092878341675, 0.8000538349151611, 0.7289119362831116, 0.6942441463470459, 0.5954713821411133, 0.47012749314308167, 0.788290798664093]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8130283951759338})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6450531482696533})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6175824403762817})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6418851613998413})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6808664798736572})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6250882148742676})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.9086, 'crossentropy': 0.5623748046875}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 8067], ['id', 18405], ['id', 13019], ['id', 13816], ['id', 31661], ['id', 33776], ['id', 9485], ['id', 2381], ['id', 9810], ['id', 33538], ['id', 18535], ['id', 28958], ['id', 17710], ['id', 56014], ['id', 36268], ['id', 41432], ['ood', 46186], ['id', 24533], ['ood', 55618], ['id', 11257]], 'labels': [8, 9, 2, 0, 0, 0, 0, 7, 9, 0, 2, 2, 3, 5, 5, 0, 5, 8, 7, 2], 'scores': [0.6069510579109192, 0.8995185494422913, 0.42485475540161133, 0.910005658864975, 0.9157633781433105, 0.9360723495483398, 0.6913127899169922, 0.6130634546279907, 1.0110127925872803, 0.7986022233963013, 1.0571025609970093, 0.44552403688430786, 0.7966293692588806, 0.6374233961105347, 0.978105902671814, 0.8869456648826599, 0.4752840995788574, 0.8667919635772705, 0.5128515958786011, 0.8212710022926331]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8083008527755737})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.552134096622467})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.515022873878479})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.592063307762146})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.574257493019104})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6385382413864136})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.9197, 'crossentropy': 0.4774974609375}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 56199], ['id', 11202], ['id', 24620], ['id', 56213], ['id', 50223], ['id', 55906], ['id', 47944], ['id', 14607], ['id', 53248], ['id', 4226], ['id', 4058], ['id', 21856], ['id', 2991], ['id', 7029], ['id', 36828], ['id', 49767], ['id', 52624], ['id', 36008], ['id', 34399], ['id', 58648]], 'labels': [9, 9, 9, 2, 5, 2, 5, 9, 8, 7, 8, 6, 8, 2, 8, 9, 1, 8, 9, 7], 'scores': [0.6304568648338318, 0.8230339288711548, 0.5875968933105469, 0.748033344745636, 0.6966042518615723, 0.7464025020599365, 0.5724973678588867, 0.40681445598602295, 0.4696505069732666, 0.5208985209465027, 0.722335934638977, 0.5845138430595398, 0.7200852632522583, 0.4916977286338806, 0.6183890700340271, 0.4503140449523926, 0.7430176734924316, 0.6441312432289124, 0.4399370551109314, 0.6833860278129578]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8745346069335938})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5848763585090637})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5110509395599365})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5212441086769104})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5244501233100891})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5134908556938171})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.9269, 'crossentropy': 0.45481181640625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 46473], ['id', 46938], ['id', 36409], ['id', 7655], ['id', 31301], ['id', 5687], ['id', 5896], ['id', 33576], ['ood', 8715], ['id', 34660], ['id', 34785], ['id', 13099], ['id', 26574], ['id', 17003], ['id', 18984], ['ood', 4942], ['id', 11631], ['id', 18042], ['id', 57195], ['id', 15803]], 'labels': [7, 7, 3, 3, 5, 3, 8, 9, 5, 3, 8, 3, 5, 0, 9, 9, 5, 0, 3, 1], 'scores': [0.5608530640602112, 0.6398107409477234, 0.6831141114234924, 0.5809599757194519, 0.7879713773727417, 0.7673576474189758, 0.49591705203056335, 0.5395330786705017, 0.5005549192428589, 0.7247739434242249, 0.8341212272644043, 0.5953106880187988, 0.5778217911720276, 0.77833092212677, 0.6405200362205505, 0.29297924041748047, 0.6904242634773254, 0.859780490398407, 0.7374151945114136, 0.7193000316619873]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8260633945465088})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5214959383010864})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4566197395324707})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.44482654333114624})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40951231122016907})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4177788496017456})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4231836199760437})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4369441270828247})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.9412, 'crossentropy': 0.3736503662109375}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 48179], ['id', 49545], ['id', 25829], ['id', 59416], ['id', 11377], ['id', 45046], ['id', 14387], ['id', 14246], ['id', 13744], ['id', 25888], ['id', 20792], ['id', 1561], ['id', 8488], ['id', 15855], ['id', 43648], ['id', 46274], ['id', 18398], ['id', 27299], ['id', 39267], ['id', 45121]], 'labels': [5, 8, 3, 3, 3, 3, 7, 7, 7, 7, 9, 2, 6, 5, 5, 7, 4, 8, 3, 4], 'scores': [0.5688691139221191, 0.8577997088432312, 0.7214868068695068, 0.4608863592147827, 0.8061357140541077, 0.5406621992588043, 0.4849010407924652, 0.8472000956535339, 0.5092597007751465, 0.7144016027450562, 0.5008503198623657, 0.5568899512290955, 0.6218130886554718, 0.8089702725410461, 0.680457592010498, 0.614183783531189, 0.8118076920509338, 0.5753622055053711, 0.7500292062759399, 0.6845925450325012]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9102293252944946})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5467987656593323})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.48966896533966064})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41839689016342163})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.49008113145828247})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4798397421836853})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4756087064743042})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9385, 'crossentropy': 0.399778564453125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 16678], ['id', 11030], ['id', 21517], ['id', 18598], ['id', 13827], ['id', 9318], ['id', 56224], ['id', 43110], ['id', 26389], ['id', 37538], ['id', 40378], ['id', 18487], ['id', 9731], ['id', 43176], ['id', 17540], ['id', 20650], ['id', 31090], ['id', 37758], ['id', 4955], ['id', 8892]], 'labels': [3, 2, 4, 9, 3, 2, 5, 8, 0, 9, 7, 4, 9, 2, 1, 4, 4, 0, 2, 8], 'scores': [0.8814389705657959, 0.610239177942276, 0.6221106648445129, 0.8323218822479248, 0.7963942289352417, 0.6802663207054138, 0.8632630109786987, 0.5426319241523743, 0.6253554821014404, 0.7288758754730225, 0.6321794986724854, 0.5780355930328369, 0.6565564274787903, 0.8352541327476501, 0.7931579947471619, 0.6559954285621643, 0.9444698691368103, 0.6841177344322205, 0.7825421690940857, 0.5464730858802795]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.063146710395813})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5908262729644775})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.424830824136734})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44913047552108765})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4861965775489807})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4002028703689575})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42159512639045715})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4286266565322876})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4422352910041809})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9473, 'crossentropy': 0.390289306640625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 2682], ['id', 27038], ['id', 42428], ['id', 50484], ['id', 138], ['id', 31757], ['id', 21666], ['id', 19837], ['id', 29206], ['id', 23962], ['id', 25508], ['id', 22818], ['id', 54954], ['id', 24990], ['id', 56457], ['id', 15261], ['id', 41713], ['id', 12268], ['id', 6843], ['id', 1674]], 'labels': [8, 5, 5, 5, 5, 2, 7, 1, 4, 3, 5, 4, 8, 7, 3, 3, 0, 8, 7, 9], 'scores': [0.6008502840995789, 0.7474181652069092, 0.9422370791435242, 0.6493121385574341, 0.8107916116714478, 0.8574306964874268, 0.7708013653755188, 0.7360413074493408, 0.6379237771034241, 0.7162479162216187, 1.046921730041504, 0.5144163072109222, 0.7267220616340637, 0.8437188267707825, 1.016394853591919, 0.6121334433555603, 0.6707567870616913, 0.8213978409767151, 0.5053642988204956, 0.8409969210624695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0358620882034302})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5684990286827087})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.46921679377555847})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39447253942489624})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4757734537124634})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40613317489624023})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40385329723358154})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9477, 'crossentropy': 0.381567529296875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 25928], ['id', 22473], ['id', 40177], ['id', 41292], ['id', 10622], ['id', 23104], ['id', 45082], ['id', 8772], ['id', 49734], ['id', 50111], ['id', 27595], ['id', 55648], ['id', 41261], ['id', 7830], ['id', 53122], ['id', 11734], ['id', 46316], ['id', 33497], ['id', 41907], ['id', 14147]], 'labels': [0, 0, 9, 2, 5, 0, 8, 1, 9, 5, 6, 9, 6, 0, 5, 8, 9, 6, 0, 6], 'scores': [0.6570377349853516, 0.7431266903877258, 0.44563567638397217, 0.5292287468910217, 0.6097735166549683, 0.6557735204696655, 0.6176084876060486, 0.637580931186676, 0.47814637422561646, 0.5974730253219604, 0.62779700756073, 0.5932068824768066, 0.506625235080719, 0.6779388189315796, 0.5967475175857544, 0.5353250503540039, 0.6210256218910217, 0.6960302591323853, 0.6158205270767212, 0.6663581728935242]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0677763223648071})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5685709714889526})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4560854732990265})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44070321321487427})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42407703399658203})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3894526958465576})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.42130473256111145})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41839414834976196})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40199825167655945})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9536, 'crossentropy': 0.354066552734375}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 9730], ['id', 5868], ['id', 27596], ['ood', 15697], ['id', 17958], ['id', 40844], ['id', 41108], ['ood', 18974], ['ood', 12355], ['id', 38698], ['id', 23406], ['id', 966], ['id', 17808], ['id', 8954], ['id', 55630], ['ood', 49536], ['id', 59747], ['id', 43126], ['ood', 28456], ['id', 33956]], 'labels': [1, 9, 8, 1, 9, 0, 0, 3, 1, 5, 4, 3, 8, 7, 4, 1, 5, 3, 1, 8], 'scores': [0.6817477941513062, 0.47871294617652893, 0.7338017225265503, 0.5715621709823608, 0.7284373641014099, 0.36942994594573975, 0.9640755653381348, 0.48980510234832764, 0.4300905466079712, 1.0107833743095398, 0.7508575320243835, 1.0958476066589355, 0.6934404969215393, 0.7201147675514221, 0.8773654103279114, 0.6496018171310425, 0.7011167705059052, 0.8370027542114258, 0.7038383483886719, 0.5365143418312073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9364936351776123})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5782960653305054})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4237990081310272})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3997109830379486})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42082417011260986})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4339101314544678})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4267749786376953})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.955, 'crossentropy': 0.3532846435546875}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 51462], ['id', 49740], ['id', 44149], ['id', 43575], ['ood', 30301], ['id', 8408], ['id', 31068], ['id', 32930], ['id', 28801], ['id', 17937], ['ood', 16455], ['id', 56499], ['ood', 13691], ['id', 13164], ['id', 50896], ['id', 57387], ['id', 3636], ['id', 23678], ['id', 5800], ['id', 24898]], 'labels': [8, 9, 2, 2, 9, 9, 2, 9, 2, 8, 8, 5, 9, 0, 9, 2, 9, 7, 8, 9], 'scores': [0.6323720216751099, 0.8248550891876221, 0.7184170484542847, 0.8895675539970398, 0.5415248870849609, 0.5691819787025452, 0.5958012342453003, 0.9288195371627808, 0.6580861806869507, 0.6847076416015625, 0.537757396697998, 0.5346001982688904, 0.4673585891723633, 0.6259091198444366, 0.4495771527290344, 0.7793552279472351, 0.6554735898971558, 0.6671711802482605, 0.5366441905498505, 0.8915446996688843]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.1305333375930786})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6245304346084595})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4387896656990051})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4423932433128357})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.38745370507240295})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.389929860830307})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38185787200927734})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3839524984359741})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39917731285095215})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3788052499294281})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3576515018939972})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40945056080818176})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4220953583717346})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41107624769210815})
store['active_learning_steps'][14]['training']['best_epoch']=11
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.956, 'crossentropy': 0.347282275390625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 148], ['id', 24337], ['id', 13242], ['id', 29179], ['id', 13861], ['id', 46658], ['id', 1642], ['ood', 50403], ['id', 24608], ['id', 22155], ['id', 26681], ['id', 17239], ['id', 51610], ['id', 5788], ['id', 29803], ['id', 12514], ['id', 58777], ['id', 5536], ['id', 39942], ['id', 19868]], 'labels': [7, 9, 3, 8, 4, 8, 6, 0, 5, 3, 8, 5, 5, 3, 6, 2, 8, 8, 9, 5], 'scores': [0.8768541812896729, 0.6108372211456299, 0.8717257976531982, 0.6689965724945068, 0.5740620493888855, 0.7523449659347534, 0.7198658585548401, 0.637551486492157, 1.0353615880012512, 0.8675740361213684, 0.8692108392715454, 0.738385021686554, 0.7113728225231171, 0.5706488490104675, 0.9598349928855896, 1.0008086562156677, 0.6073866486549377, 0.8563831448554993, 0.7865757346153259, 1.0371791124343872]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1811769008636475})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5857483148574829})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43590086698532104})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3789471685886383})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35627293586730957})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3630926012992859})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32680875062942505})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.340168833732605})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35809487104415894})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34504175186157227})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9584, 'crossentropy': 0.309824853515625}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 42415], ['id', 38389], ['id', 52306], ['id', 43702], ['id', 33796], ['id', 52808], ['id', 20110], ['id', 57054], ['id', 17478], ['id', 43979], ['id', 21944], ['id', 56162], ['id', 16698], ['id', 37773], ['id', 33594], ['id', 49950], ['id', 59294], ['id', 44172], ['id', 55128], ['id', 31252]], 'labels': [7, 7, 8, 3, 7, 8, 4, 8, 4, 6, 1, 6, 5, 9, 3, 5, 8, 8, 8, 5], 'scores': [0.8610256910324097, 0.6073620021343231, 0.8076038360595703, 0.8055868744850159, 0.6894568502902985, 0.6993297934532166, 0.7040566802024841, 0.4670403003692627, 0.6652984619140625, 0.48307132720947266, 0.6576318144798279, 0.585899144411087, 0.6482181251049042, 0.6454652547836304, 0.8179008960723877, 0.5237567126750946, 1.1204186081886292, 0.6448793411254883, 0.8851553201675415, 0.6428560614585876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1608946323394775})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5827924013137817})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4073414206504822})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3583804965019226})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3535670042037964})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3208569288253784})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3638538718223572})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39133405685424805})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35223719477653503})
store['active_learning_steps'][16]['training']['best_epoch']=6
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9654, 'crossentropy': 0.29051484375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 25137], ['id', 36527], ['id', 45502], ['id', 28190], ['id', 3692], ['id', 13078], ['id', 17503], ['id', 2248], ['id', 4827], ['id', 30240], ['id', 36421], ['id', 41662], ['id', 52661], ['id', 55274], ['id', 33408], ['id', 46854], ['id', 45586], ['id', 27556], ['id', 41156], ['id', 27172]], 'labels': [0, 6, 1, 4, 7, 5, 0, 5, 6, 0, 3, 2, 3, 6, 7, 3, 3, 6, 0, 3], 'scores': [0.5589827597141266, 0.6893058121204376, 0.6230691075325012, 0.6035367846488953, 0.6640422344207764, 0.6994497179985046, 0.6285903453826904, 0.5313280820846558, 0.507975697517395, 0.3895151913166046, 0.8189818859100342, 0.6236423850059509, 0.5861096978187561, 0.627228856086731, 0.6018975973129272, 0.3909047544002533, 0.6196522116661072, 0.5933817028999329, 0.588469535112381, 0.7775853276252747]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0161443948745728})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.55243980884552})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4549674391746521})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35696715116500854})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33526700735092163})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31228071451187134})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32322457432746887})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36417660117149353})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3330274820327759})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9637, 'crossentropy': 0.2863280517578125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 55314], ['id', 20211], ['id', 1518], ['id', 6808], ['id', 43874], ['id', 2818], ['id', 22133], ['id', 43268], ['id', 52456], ['id', 20660], ['id', 6085], ['id', 33918], ['id', 4139], ['id', 55958], ['id', 54885], ['id', 52173], ['id', 5928], ['id', 55739], ['id', 43042], ['id', 3762]], 'labels': [6, 4, 9, 8, 2, 3, 2, 8, 2, 8, 6, 1, 8, 5, 6, 7, 2, 5, 8, 8], 'scores': [0.4859505295753479, 0.6394476890563965, 0.5319771766662598, 0.7474756836891174, 0.6383323073387146, 0.6052370071411133, 0.5607077479362488, 0.5311815440654755, 0.5334348678588867, 0.6770798563957214, 0.40728890895843506, 0.612028956413269, 0.46362531185150146, 0.6850113272666931, 0.4984167218208313, 0.5892542004585266, 0.5851541757583618, 0.5646449327468872, 0.5826327800750732, 0.6486064791679382]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.2394943237304688})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6616917848587036})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.48441293835639954})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5010464191436768})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3512231707572937})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3480243682861328})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33565765619277954})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3530194163322449})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3438599109649658})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3302348256111145})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3894473910331726})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3506135046482086})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34456199407577515})
store['active_learning_steps'][18]['training']['best_epoch']=10
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9665, 'crossentropy': 0.2957073486328125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 5295], ['id', 35205], ['id', 39427], ['id', 2622], ['id', 14722], ['id', 49426], ['id', 30062], ['id', 50562], ['id', 34771], ['ood', 23684], ['id', 50317], ['id', 32445], ['id', 47283], ['id', 45069], ['id', 15913], ['id', 22320], ['id', 3094], ['id', 36884], ['id', 23996], ['id', 46369]], 'labels': [4, 6, 5, 5, 0, 6, 3, 9, 0, 8, 3, 5, 8, 4, 9, 8, 8, 2, 5, 5], 'scores': [0.8944494724273682, 0.912941038608551, 0.8536745309829712, 0.899901807308197, 0.9402201771736145, 0.6797088384628296, 0.8654319047927856, 1.060806691646576, 0.8548815846443176, 0.5204962491989136, 1.0149054527282715, 0.9013902544975281, 0.48858895897865295, 0.8098005056381226, 0.8767816424369812, 0.8051362037658691, 0.617630124092102, 0.7817859053611755, 0.37149493396282196, 0.9324353933334351]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1298339366912842})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.675019383430481})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4586789906024933})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35831761360168457})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39779770374298096})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30286988615989685})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3382839858531952})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37142282724380493})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3729161322116852})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.277744775390625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 13714], ['id', 26636], ['id', 49088], ['id', 46734], ['id', 53568], ['id', 16209], ['id', 2928], ['id', 43424], ['id', 38246], ['id', 21601], ['id', 958], ['id', 29002], ['id', 7808], ['id', 3955], ['id', 1181], ['id', 12078], ['id', 15432], ['id', 14100], ['id', 41060], ['id', 5260]], 'labels': [4, 5, 8, 4, 5, 2, 5, 6, 7, 1, 6, 7, 7, 1, 1, 1, 4, 5, 6, 6], 'scores': [0.6534005403518677, 0.5200797319412231, 0.5429695844650269, 0.5384179949760437, 0.7453228235244751, 0.5016767978668213, 0.7677573561668396, 0.5732713341712952, 0.48654794692993164, 0.5708763599395752, 0.4663032591342926, 0.5976659059524536, 0.5087047815322876, 0.45831578969955444, 0.45313572883605957, 0.42634743452072144, 0.5274322032928467, 0.46405261754989624, 0.632968008518219, 0.6699890494346619]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9748899936676025})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5686898231506348})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.45533400774002075})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32546669244766235})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32116150856018066})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28649941086769104})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2986237406730652})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31029507517814636})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30379587411880493})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9717, 'crossentropy': 0.2552947998046875}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 45944], ['id', 36065], ['id', 28293], ['id', 37347], ['id', 13928], ['id', 44298], ['id', 1260], ['id', 15779], ['id', 4062], ['id', 34078], ['id', 45576], ['id', 24462], ['ood', 7862], ['id', 1838], ['id', 52834], ['id', 11668], ['ood', 26190], ['id', 40704], ['id', 14896], ['id', 56379]], 'labels': [9, 5, 2, 2, 2, 2, 3, 0, 5, 2, 8, 2, 9, 1, 2, 9, 7, 5, 8, 4], 'scores': [0.6487270593643188, 0.7150816917419434, 0.7195122838020325, 0.8976848721504211, 0.7216368913650513, 0.7256680130958557, 0.39004212617874146, 0.8839773535728455, 0.6632810831069946, 0.6622413992881775, 0.5381757020950317, 0.6947911977767944, 0.404238224029541, 0.29029178619384766, 0.8546323776245117, 0.5437465310096741, 0.49966955184936523, 0.5369350910186768, 0.7260662317276001, 0.6040924787521362]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.2309467792510986})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.6076842546463013})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45721983909606934})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3549760580062866})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33520299196243286})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2865208089351654})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29305005073547363})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26697206497192383})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27690741419792175})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27953314781188965})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26881569623947144})
store['active_learning_steps'][21]['training']['best_epoch']=8
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9699, 'crossentropy': 0.2474982177734375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 22501], ['id', 53694], ['id', 32342], ['id', 4612], ['id', 21426], ['id', 48349], ['id', 52838], ['id', 49515], ['id', 49958], ['id', 54782], ['id', 45091], ['id', 8780], ['id', 17079], ['id', 18904], ['id', 35051], ['id', 21956], ['id', 9940], ['id', 16219], ['id', 2872], ['id', 22491]], 'labels': [9, 7, 9, 6, 6, 2, 4, 2, 7, 3, 5, 8, 6, 6, 2, 5, 4, 5, 1, 2], 'scores': [0.6803215146064758, 0.6422921419143677, 0.5828798413276672, 0.253415048122406, 0.6374243497848511, 0.7528363466262817, 0.7788099050521851, 0.7031969428062439, 0.8588224351406097, 0.6402648687362671, 0.5155062675476074, 0.7078187465667725, 0.9093091487884521, 0.4837595224380493, 0.5833700895309448, 0.8279826641082764, 0.5467846393585205, 0.6232462525367737, 0.5585023760795593, 0.6762112975120544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0287108421325684})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5695570111274719})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42071080207824707})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3360106348991394})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.303405225276947})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27645623683929443})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29132547974586487})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23320558667182922})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2517789900302887})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24688974022865295})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2398160845041275})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9746, 'crossentropy': 0.2256767333984375}
