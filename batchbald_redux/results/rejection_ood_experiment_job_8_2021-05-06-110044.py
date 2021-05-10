store = {}
store['timestamp']=1620295244
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=8']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=8
store['worker_id']=8
store['num_workers']=40
store['config']={'seed': 10, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.4238171577453613})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.956916570663452})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.213360548019409})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.2559003829956055})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6568, 'crossentropy': 2.223854296875}
store['active_learning_steps'][0]['acquisition']={'indices': [35339, 23042, 6331, 8358, 9345], 'labels': [8, 9, 0, 9, 8], 'scores': [1.1628767848014832, 1.154166579246521, 1.1520371437072754, 1.1487714648246765, 1.1485024690628052]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.1036605834960938})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.316620349884033})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.163337230682373})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.887878894805908})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7102, 'crossentropy': 1.8321947265625}
store['active_learning_steps'][1]['acquisition']={'indices': [46707, 28391, 29246, 47683, 10012], 'labels': [2, 3, 3, 5, 8], 'scores': [1.1596647500991821, 1.1448312401771545, 1.13930743932724, 1.1327720880508423, 1.1160269975662231]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7647101879119873})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.9848086833953857})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.454448699951172})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.3045477867126465})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7083, 'crossentropy': 1.6856443359375}
store['active_learning_steps'][2]['acquisition']={'indices': [11304, 34706, 25644, 56174, 53116], 'labels': [0, 0, 4, 0, 0], 'scores': [1.1144822835922241, 1.0390117764472961, 1.0380731225013733, 1.0293214321136475, 1.022498369216919]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.9598362445831299})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.1104090213775635})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.118457317352295})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.367987871170044})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7011, 'crossentropy': 1.701388671875}
store['active_learning_steps'][3]['acquisition']={'indices': [28520, 10038, 27219, 3382, 37793], 'labels': [7, 9, 7, 9, 4], 'scores': [1.0589606165885925, 1.0391314625740051, 1.0390594601631165, 1.0320733189582825, 1.0201261043548584]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.6850377321243286})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.733384132385254})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.984173059463501})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 2.0739011764526367})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7808, 'crossentropy': 1.4184484375}
store['active_learning_steps'][4]['acquisition']={'indices': [15093, 44267, 46293, 11025, 17269], 'labels': [2, 8, 2, 5, 2], 'scores': [1.1590070724487305, 1.117749571800232, 1.1108751893043518, 1.0952963829040527, 1.0938647985458374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.5588375329971313})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.749221920967102})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.99791419506073})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.8925235271453857})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7474, 'crossentropy': 1.3693181640625}
store['active_learning_steps'][5]['acquisition']={'indices': [47028, 9468, 50269, 57985, 16532], 'labels': [4, 6, 7, 4, 2], 'scores': [0.9045522212982178, 0.9013646841049194, 0.9005456566810608, 0.8942016959190369, 0.8940390348434448]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.2683939933776855})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.5548640489578247})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.7305630445480347})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.6734687089920044})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7894, 'crossentropy': 1.0922626953125}
store['active_learning_steps'][6]['acquisition']={'indices': [44040, 37181, 1239, 16033, 6725], 'labels': [0, 5, 8, 2, 2], 'scores': [0.9029412865638733, 0.9005593061447144, 0.8875337839126587, 0.887139081954956, 0.8658377528190613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.4750477075576782})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.597841501235962})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.5898836851119995})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.699472188949585})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.772, 'crossentropy': 1.2421107421875}
store['active_learning_steps'][7]['acquisition']={'indices': [9428, 2636, 44944, 31962, 15562], 'labels': [9, 8, 8, 3, 9], 'scores': [1.0300022959709167, 1.022650122642517, 1.018974781036377, 1.0060657262802124, 0.9937893152236938]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.2881824970245361})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.5534672737121582})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.7597520351409912})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.809403896331787})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7678, 'crossentropy': 1.16050615234375}
store['active_learning_steps'][8]['acquisition']={'indices': [969, 15833, 981, 46368, 15705], 'labels': [7, 7, 7, 8, 7], 'scores': [0.8414970636367798, 0.8227338194847107, 0.8151865005493164, 0.7952526807785034, 0.7911763191223145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.2250885963439941})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.4948980808258057})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.4353276491165161})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.5765537023544312})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7812, 'crossentropy': 1.09598466796875}
store['active_learning_steps'][9]['acquisition']={'indices': [23734, 24219, 10492, 12345, 53472], 'labels': [5, 3, 5, 3, 6], 'scores': [0.8895078301429749, 0.881195604801178, 0.841978907585144, 0.8398844599723816, 0.8333625793457031]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.1586582660675049})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.3970985412597656})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.3884443044662476})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.581776738166809})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8031, 'crossentropy': 0.9872173828125}
store['active_learning_steps'][10]['acquisition']={'indices': [50052, 5045, 31926, 13652, 5684], 'labels': [2, 9, 5, 9, 6], 'scores': [0.8640682101249695, 0.8575802445411682, 0.8404901027679443, 0.8379936218261719, 0.8295704126358032]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.179706335067749})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.3008091449737549})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.3730649948120117})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3420612812042236})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7851, 'crossentropy': 1.00217734375}
store['active_learning_steps'][11]['acquisition']={'indices': [9403, 28412, 8978, 3719, 52771], 'labels': [3, 0, 2, 2, 3], 'scores': [0.7847528457641602, 0.781884491443634, 0.7799832820892334, 0.771852970123291, 0.7584010362625122]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.211025595664978})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.2682701349258423})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.3578068017959595})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.493536353111267})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.792, 'crossentropy': 1.01569443359375}
store['active_learning_steps'][12]['acquisition']={'indices': [55591, 28040, 39963, 25391, 22269], 'labels': [5, 5, 4, 5, 2], 'scores': [0.8661110401153564, 0.8115742206573486, 0.8106131553649902, 0.8042917251586914, 0.8003853559494019]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0702729225158691})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.156778335571289})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.2996861934661865})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3453090190887451})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.809, 'crossentropy': 0.94628505859375}
store['active_learning_steps'][13]['acquisition']={'indices': [50443, 47741, 7168, 54194, 5474], 'labels': [7, 5, 8, 7, 8], 'scores': [0.7607008218765259, 0.7419082522392273, 0.7287284135818481, 0.7273449301719666, 0.7228028774261475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.0292229652404785})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9788873195648193})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1957247257232666})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9903645515441895})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2024638652801514})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8588, 'crossentropy': 0.830728125}
store['active_learning_steps'][14]['acquisition']={'indices': [51544, 3070, 36744, 17756, 53228], 'labels': [1, 1, 1, 8, 6], 'scores': [1.0750097036361694, 1.0046184659004211, 0.9670418500900269, 0.9536157846450806, 0.9375161528587341]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9872221946716309})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9538723230361938})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9298197031021118})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.018021821975708})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9911878108978271})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.092724084854126})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8652, 'crossentropy': 0.87080869140625}
store['active_learning_steps'][15]['acquisition']={'indices': [15893, 37214, 19616, 28199, 36998], 'labels': [5, 2, 9, 3, 2], 'scores': [1.0315033197402954, 1.0177847743034363, 1.0150930285453796, 0.9983518123626709, 0.9965888857841492]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.0273675918579102})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8862833380699158})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0020285844802856})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.054331660270691})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0660936832427979})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8685, 'crossentropy': 0.75348857421875}
store['active_learning_steps'][16]['acquisition']={'indices': [4701, 23020, 14113, 17710, 54043], 'labels': [2, 2, 2, 3, 2], 'scores': [1.013432264328003, 0.9644421935081482, 0.962351381778717, 0.9290429949760437, 0.9277332425117493]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.044980764389038})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0656245946884155})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9196420907974243})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0690174102783203})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1786161661148071})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.2588069438934326})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8598, 'crossentropy': 0.82740361328125}
store['active_learning_steps'][17]['acquisition']={'indices': [19590, 12236, 21012, 30441, 2856], 'labels': [5, 1, 2, 1, 4], 'scores': [1.0150773525238037, 0.9960123300552368, 0.9924477934837341, 0.9878240823745728, 0.9855926036834717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0005406141281128})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8535370826721191})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8639522790908813})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8406470417976379})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8549652099609375})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9599356055259705})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9380776882171631})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8945, 'crossentropy': 0.69663740234375}
store['active_learning_steps'][18]['acquisition']={'indices': [5728, 31664, 23490, 42703, 14749], 'labels': [3, 3, 3, 0, 0], 'scores': [1.0178077220916748, 1.000753939151764, 0.9998675584793091, 0.9988943934440613, 0.9976742267608643]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9360443949699402})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8552943468093872})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.945753276348114})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9145944118499756})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9101256132125854})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8868, 'crossentropy': 0.696861279296875}
store['active_learning_steps'][19]['acquisition']={'indices': [49354, 42020, 51492, 39700, 21355], 'labels': [0, 9, 5, 5, 0], 'scores': [0.9461673498153687, 0.9416722655296326, 0.9293206930160522, 0.9205783605575562, 0.9102113246917725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.958989143371582})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8166370987892151})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8147923946380615})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8388821482658386})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9290060997009277})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9026503562927246})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8938, 'crossentropy': 0.69653642578125}
store['active_learning_steps'][20]['acquisition']={'indices': [47597, 50343, 44736, 44255, 5626], 'labels': [8, 6, 5, 6, 7], 'scores': [1.067294716835022, 1.0141621232032776, 0.9948911070823669, 0.9865745306015015, 0.9863764047622681]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0060453414916992})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7332484722137451})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7257583141326904})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7868388295173645})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7610416412353516})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7875404953956604})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9028, 'crossentropy': 0.662210302734375}
store['active_learning_steps'][21]['acquisition']={'indices': [42828, 7933, 5315, 46088, 24479], 'labels': [7, 2, 3, 6, 8], 'scores': [1.0497292280197144, 1.0430819988250732, 1.0331048965454102, 1.0204464793205261, 1.0154088735580444]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8713454008102417})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7354543805122375})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6634947657585144})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7351094484329224})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7341095209121704})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7866265177726746})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9085, 'crossentropy': 0.58886005859375}
store['active_learning_steps'][22]['acquisition']={'indices': [42799, 46878, 29493, 48681, 34445], 'labels': [2, 5, 8, 2, 7], 'scores': [1.0478177070617676, 1.0095983743667603, 0.9704936742782593, 0.9662567377090454, 0.9519778490066528]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8807153105735779})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6714429259300232})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6587475538253784})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.627617359161377})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7301074862480164})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7297384738922119})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8496764898300171})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.60624501953125}
store['active_learning_steps'][23]['acquisition']={'indices': [21880, 2465, 11539, 8932, 45917], 'labels': [2, 9, -1, 0, 9], 'scores': [1.026126503944397, 1.002377450466156, 0.9953346848487854, 0.98602694272995, 0.9790967702865601]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9192348718643188})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6658595204353333})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6579588651657104})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8244533538818359})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6798915863037109})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.78163743019104})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9059, 'crossentropy': 0.624262255859375}
store['active_learning_steps'][24]['acquisition']={'indices': [20171, 32335, 24160, 32323, 29972], 'labels': [5, 1, 8, 5, 3], 'scores': [0.9963020086288452, 0.9929618239402771, 0.968489408493042, 0.9630444645881653, 0.959540843963623]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.879133939743042})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6262287497520447})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5869507193565369})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6931842565536499})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6658043265342712})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7605783343315125})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9252, 'crossentropy': 0.53540712890625}
store['active_learning_steps'][25]['acquisition']={'indices': [57728, 4822, 30622, 35401, 51854], 'labels': [9, 4, 5, 3, 5], 'scores': [0.9925597310066223, 0.9838671684265137, 0.9827759265899658, 0.9813167452812195, 0.977525532245636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8690923452377319})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6379103660583496})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6140999794006348})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5562644004821777})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7111091017723083})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6649897694587708})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6421723961830139})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9336, 'crossentropy': 0.483068212890625}
store['active_learning_steps'][26]['acquisition']={'indices': [44865, 22513, 7768, 5052, 50930], 'labels': [7, 7, 8, 0, 0], 'scores': [0.9790756106376648, 0.9650452733039856, 0.9342284202575684, 0.9311758875846863, 0.9216201901435852]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0140661001205444})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6843826770782471})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6153308153152466})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6049560308456421})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6048116683959961})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7116310596466064})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6618230938911438})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6847138404846191})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9186, 'crossentropy': 0.540865869140625}
store['active_learning_steps'][27]['acquisition']={'indices': [46530, 23350, 13945, 52151, 34406], 'labels': [4, 8, 9, 9, 4], 'scores': [1.0660671591758728, 1.0214887857437134, 1.0168622136116028, 1.0110707879066467, 1.0064289569854736]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8452816605567932})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6327539682388306})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6365659236907959})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6144812703132629})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6341955065727234})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6583667993545532})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7044532299041748})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9278, 'crossentropy': 0.53491396484375}
store['active_learning_steps'][28]['acquisition']={'indices': [12986, 33812, 52582, 49525, 20606], 'labels': [5, 6, 2, 8, 3], 'scores': [0.9960956573486328, 0.9781519770622253, 0.966298520565033, 0.9654375314712524, 0.9632846117019653]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9347642660140991})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5315070152282715})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5607801675796509})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6168649196624756})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6186481714248657})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9206, 'crossentropy': 0.54481123046875}
store['active_learning_steps'][29]['acquisition']={'indices': [42221, 25384, 41608, 57972, 26444], 'labels': [5, 5, -1, 4, 1], 'scores': [0.9168516993522644, 0.8980305790901184, 0.8621044158935547, 0.8567546606063843, 0.8557215332984924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8798319101333618})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5876374244689941})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5513733625411987})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5366809368133545})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5851810574531555})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5532937049865723})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6908431053161621})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9309, 'crossentropy': 0.491626513671875}
store['active_learning_steps'][30]['acquisition']={'indices': [32387, 22083, 56662, 10258, 12497], 'labels': [4, 2, 0, 5, 0], 'scores': [1.0513219237327576, 0.9806389808654785, 0.974161684513092, 0.9686112999916077, 0.9626429080963135]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9551334381103516})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5393550395965576})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4848875105381012})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4910372793674469})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5192548632621765})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5329025983810425})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9325, 'crossentropy': 0.462058935546875}
store['active_learning_steps'][31]['acquisition']={'indices': [52169, 52801, 36704, 20641, 37403], 'labels': [2, 2, 2, 9, 2], 'scores': [1.0544724464416504, 0.966666042804718, 0.9599279165267944, 0.9455534219741821, 0.9109410047531128]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.93522047996521})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5535973906517029})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5395393371582031})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.611558198928833})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.60317063331604})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5822068452835083})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9243, 'crossentropy': 0.493048193359375}
store['active_learning_steps'][32]['acquisition']={'indices': [22272, 41295, 59289, 25462, 39818], 'labels': [5, 9, 1, 6, 1], 'scores': [0.9483665823936462, 0.904680073261261, 0.8857262134552002, 0.8855183124542236, 0.8746270537376404]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9677689075469971})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6260026693344116})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5591425895690918})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5716410279273987})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6027216911315918})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6138362884521484})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9205, 'crossentropy': 0.496133251953125}
store['active_learning_steps'][33]['acquisition']={'indices': [424, 45047, 7879, 43212, 36126], 'labels': [9, 2, 2, 5, 5], 'scores': [0.958338737487793, 0.9105730652809143, 0.8948370218276978, 0.8747375011444092, 0.8732481002807617]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9921447038650513})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5721975564956665})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5331092476844788})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49043354392051697})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5495348572731018})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5705211162567139})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5850876569747925})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9291, 'crossentropy': 0.475212548828125}
store['active_learning_steps'][34]['acquisition']={'indices': [16059, 59783, 44570, 7207, 8879], 'labels': [8, 1, 7, 2, 3], 'scores': [0.9693898558616638, 0.9528634548187256, 0.9463666081428528, 0.9433444738388062, 0.9385911226272583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1192131042480469})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6104938983917236})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.565218448638916})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5824170112609863})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5406873822212219})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5750934481620789})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.593570351600647})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.631528913974762})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9355, 'crossentropy': 0.462403759765625}
store['active_learning_steps'][35]['acquisition']={'indices': [9118, 11572, 40589, 47870, 10524], 'labels': [9, 5, 2, 9, 9], 'scores': [1.083954393863678, 1.000260055065155, 0.9874393939971924, 0.9834302067756653, 0.9810864925384521]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0110819339752197})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6256438493728638})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5627235174179077})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5410999059677124})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5424917936325073})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5721431374549866})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6082642078399658})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9301, 'crossentropy': 0.485696826171875}
store['active_learning_steps'][36]['acquisition']={'indices': [24424, 32880, 20989, 45602, 57523], 'labels': [1, 0, 3, 5, 3], 'scores': [0.9711160659790039, 0.9412919282913208, 0.9349982738494873, 0.9304664731025696, 0.9143765568733215]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0057857036590576})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6113972067832947})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.514928936958313})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5349897146224976})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5892961025238037})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6198349595069885})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9266, 'crossentropy': 0.476913330078125}
store['active_learning_steps'][37]['acquisition']={'indices': [23962, 46412, 16756, 3810, 30884], 'labels': [3, 0, 7, 3, 2], 'scores': [0.8937327861785889, 0.8857710361480713, 0.8769952654838562, 0.8701748251914978, 0.8680906891822815]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9475972056388855})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5879921913146973})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5893558263778687})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4477733373641968})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5201835036277771})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5308866500854492})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5494863390922546})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9378, 'crossentropy': 0.4204330078125}
store['active_learning_steps'][38]['acquisition']={'indices': [43224, 40312, 22561, 9147, 22497], 'labels': [3, 0, 6, 4, 7], 'scores': [0.8841458559036255, 0.8416702747344971, 0.838645875453949, 0.8358224034309387, 0.8346462249755859]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.2531554698944092})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7069199085235596})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5500578880310059})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5547661781311035})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5946946144104004})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6044412851333618})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9287, 'crossentropy': 0.472886572265625}
store['active_learning_steps'][39]['acquisition']={'indices': [37048, 42415, 13318, 10044, 10746], 'labels': [9, 7, 6, 6, 9], 'scores': [1.0879763960838318, 0.9110169410705566, 0.884423017501831, 0.8822911977767944, 0.8690162897109985]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1130759716033936})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6758904457092285})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5226351618766785})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5606275796890259})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.620506763458252})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5998402833938599})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9231, 'crossentropy': 0.49974365234375}
store['active_learning_steps'][40]['acquisition']={'indices': [46927, 57308, 59280, 18739, 50320], 'labels': [8, 3, 8, 3, 5], 'scores': [0.7986702919006348, 0.7979544997215271, 0.7969249486923218, 0.7957945466041565, 0.7952038645744324]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0731956958770752})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.599291980266571})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5072339177131653})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48019492626190186})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5822770595550537})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5764381885528564})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5085570812225342})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9374, 'crossentropy': 0.44006181640625}
store['active_learning_steps'][41]['acquisition']={'indices': [5175, 12337, 1423, 42317, 37469], 'labels': [4, 0, 0, 5, 2], 'scores': [0.9816590547561646, 0.9802449941635132, 0.9762804508209229, 0.9760591983795166, 0.9592040777206421]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1048814058303833})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6241352558135986})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.469155877828598})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5155166387557983})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5447354316711426})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4727809727191925})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9336, 'crossentropy': 0.4765693359375}
store['active_learning_steps'][42]['acquisition']={'indices': [40466, 34520, 55314, 12792, 41078], 'labels': [8, 6, 6, 9, 8], 'scores': [0.8383113145828247, 0.8360670208930969, 0.8207554817199707, 0.8178967237472534, 0.8164635300636292]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.055662751197815})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6501866579055786})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5005922317504883})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46716225147247314})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4728255867958069})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5530368089675903})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4921318590641022})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.934, 'crossentropy': 0.4669521484375}
store['active_learning_steps'][43]['acquisition']={'indices': [14062, 59747, 50097, 52462, 43897], 'labels': [8, 5, 8, 9, 1], 'scores': [0.953798770904541, 0.9403458833694458, 0.9226570129394531, 0.9212098121643066, 0.898407518863678]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1773886680603027})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5820953249931335})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5304948091506958})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.491098016500473})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4779580235481262})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45365357398986816})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5606200695037842})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5676193237304688})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4843319058418274})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9438, 'crossentropy': 0.42325009765625}
store['active_learning_steps'][44]['acquisition']={'indices': [5129, 4741, 26358, 18487, 57718], 'labels': [2, 6, 3, 4, 7], 'scores': [0.9874187707901001, 0.968092679977417, 0.9255025386810303, 0.916102945804596, 0.9031385779380798]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.2004338502883911})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6527038812637329})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5340590476989746})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5458143949508667})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5404020547866821})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5561397075653076})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9308, 'crossentropy': 0.513700390625}
store['active_learning_steps'][45]['acquisition']={'indices': [43692, 19720, 24587, 58560, 31881], 'labels': [8, 8, 8, 0, 8], 'scores': [0.8686594367027283, 0.8471024632453918, 0.8253246545791626, 0.8013564348220825, 0.7989771366119385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.1888225078582764})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7249007225036621})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4977688789367676})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5615471601486206})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.553794264793396})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4791703522205353})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48616236448287964})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46594613790512085})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5507871508598328})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5529969930648804})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49359074234962463})
store['active_learning_steps'][46]['training']['best_epoch']=8
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.937, 'crossentropy': 0.462932470703125}
store['active_learning_steps'][46]['acquisition']={'indices': [21636, 13428, 30811, 43941, 6291], 'labels': [2, 9, 2, 0, 3], 'scores': [1.035764455795288, 1.02278071641922, 0.973580539226532, 0.970215380191803, 0.9692825078964233]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.2135089635849})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6759072542190552})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49441519379615784})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5119577646255493})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4270504117012024})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43312862515449524})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4924222230911255})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4360398054122925})
store['active_learning_steps'][47]['training']['best_epoch']=5
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9475, 'crossentropy': 0.3900379638671875}
store['active_learning_steps'][47]['acquisition']={'indices': [38050, 43588, 49515, 15771, 12297], 'labels': [6, 8, 2, 5, 9], 'scores': [0.8988035917282104, 0.8899503946304321, 0.8727437257766724, 0.8371264338493347, 0.8322433829307556]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.1557021141052246})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5952782034873962})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5164690017700195})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4985647201538086})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4629519283771515})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5047603249549866})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48856469988822937})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.557823657989502})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9445, 'crossentropy': 0.435280078125}
store['active_learning_steps'][48]['acquisition']={'indices': [22480, 50736, 8228, 37078, 7949], 'labels': [4, -1, 3, 8, -1], 'scores': [0.9597240686416626, 0.920700192451477, 0.9186872243881226, 0.8969296813011169, 0.8949146270751953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.082114815711975})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6532355546951294})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5242188572883606})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5222757458686829})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5224717855453491})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4557236433029175})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.551044225692749})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5245828628540039})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5180959701538086})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9365, 'crossentropy': 0.456603564453125}
store['active_learning_steps'][49]['acquisition']={'indices': [22607, 32776, 28392, 50317, 39668], 'labels': [4, 4, 3, 3, 8], 'scores': [0.9150235652923584, 0.9113513231277466, 0.905655026435852, 0.8887850046157837, 0.8774427175521851]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1427056789398193})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.653595507144928})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.49086642265319824})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47461438179016113})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5538406372070312})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.46156466007232666})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.49481838941574097})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47324690222740173})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5382168292999268})
store['active_learning_steps'][50]['training']['best_epoch']=6
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9443, 'crossentropy': 0.42846953125}
store['active_learning_steps'][50]['acquisition']={'indices': [20110, 49200, 57628, 57714, 1075], 'labels': [4, 0, 2, 1, 7], 'scores': [0.9605758786201477, 0.9575543999671936, 0.9550820589065552, 0.9533149600028992, 0.9504073262214661]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.1906273365020752})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6487613916397095})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5215098857879639})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4793305993080139})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5205115079879761})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5023016929626465})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4956687092781067})
store['active_learning_steps'][51]['training']['best_epoch']=4
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9397, 'crossentropy': 0.462242138671875}
store['active_learning_steps'][51]['acquisition']={'indices': [39405, 53872, 36818, 31301, 25839], 'labels': [5, 8, 7, 5, 0], 'scores': [0.9175242185592651, 0.8389867544174194, 0.8362127542495728, 0.8260228633880615, 0.8244401216506958]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.324696660041809})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6839516758918762})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5858315825462341})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.46458500623703003})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5258896350860596})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5187394618988037})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5288169384002686})
store['active_learning_steps'][52]['training']['best_epoch']=4
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9418, 'crossentropy': 0.44767900390625}
store['active_learning_steps'][52]['acquisition']={'indices': [12066, 20037, 32047, 2450, 15450], 'labels': [8, 8, 9, 2, 6], 'scores': [0.8065760731697083, 0.804097056388855, 0.7965741157531738, 0.7947642505168915, 0.7903563976287842]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.336916208267212})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7204574942588806})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5513213872909546})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5066415071487427})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5012353658676147})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.463333398103714})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5438284873962402})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5035691857337952})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5200822353363037})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9427, 'crossentropy': 0.441074462890625}
store['active_learning_steps'][53]['acquisition']={'indices': [39575, 31761, 17055, 11292, 54858], 'labels': [8, 4, 8, 1, 3], 'scores': [0.9262814521789551, 0.9174917936325073, 0.9048275351524353, 0.8930416703224182, 0.8917025923728943]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.268754005432129})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6893917322158813})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5414110422134399})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5322985649108887})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4831438660621643})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5023935437202454})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.503568172454834})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47429358959198})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5425654649734497})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.49635034799575806})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5191529989242554})
store['active_learning_steps'][54]['training']['best_epoch']=8
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9504, 'crossentropy': 0.4033654052734375}
store['active_learning_steps'][54]['acquisition']={'indices': [30900, 34188, 21896, 21601, 16836], 'labels': [5, 3, 8, 1, 7], 'scores': [1.0502191185951233, 0.9817584753036499, 0.9774043560028076, 0.9711096882820129, 0.9689350724220276]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.3290996551513672})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7223473787307739})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5508851408958435})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4572073817253113})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45887190103530884})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44931161403656006})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4591204524040222})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.48329466581344604})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5015671253204346})
store['active_learning_steps'][55]['training']['best_epoch']=6
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9432, 'crossentropy': 0.431385888671875}
store['active_learning_steps'][55]['acquisition']={'indices': [17478, 886, 18324, 45502, 6524], 'labels': [4, 5, 0, 1, 5], 'scores': [0.9397882223129272, 0.9185794591903687, 0.912510871887207, 0.903156042098999, 0.9003536105155945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.339747428894043})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6552929282188416})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5203653573989868})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5014016032218933})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49787217378616333})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4583187699317932})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5598190426826477})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48246896266937256})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5449091196060181})
store['active_learning_steps'][56]['training']['best_epoch']=6
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9431, 'crossentropy': 0.44561533203125}
store['active_learning_steps'][56]['acquisition']={'indices': [29511, 13942, 26568, 52590, 15913], 'labels': [-1, 4, -1, -1, 9], 'scores': [0.920617938041687, 0.9148571491241455, 0.9093793630599976, 0.9054608345031738, 0.9033833742141724]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2948131561279297})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7442927360534668})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5431052446365356})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44652387499809265})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45516204833984375})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42620187997817993})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.43441879749298096})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.47266170382499695})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44420063495635986})
store['active_learning_steps'][57]['training']['best_epoch']=6
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.95, 'crossentropy': 0.3837985107421875}
store['active_learning_steps'][57]['acquisition']={'indices': [52140, 14385, 40259, 670, 15723], 'labels': [4, 8, 8, 3, 8], 'scores': [0.9749390482902527, 0.9320918917655945, 0.9275294542312622, 0.9145281314849854, 0.9036094546318054]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.253791332244873})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6564039587974548})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5487010478973389})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45461899042129517})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4429324269294739})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.43620508909225464})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41979286074638367})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4299323558807373})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4102139472961426})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4620078206062317})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4794047474861145})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.48374271392822266})
store['active_learning_steps'][58]['training']['best_epoch']=9
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.95, 'crossentropy': 0.411576416015625}
store['active_learning_steps'][58]['acquisition']={'indices': [49563, 19998, 12940, 41772, 24325], 'labels': [8, -1, 5, 5, -1], 'scores': [1.0594947338104248, 1.0113162994384766, 1.008055329322815, 1.0064367055892944, 1.0040611028671265]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.2114439010620117})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5852032899856567})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4815436601638794})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4586523175239563})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4056559205055237})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4352853000164032})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38205966353416443})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36646339297294617})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47338414192199707})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45310327410697937})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41414254903793335})
store['active_learning_steps'][59]['training']['best_epoch']=8
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9498, 'crossentropy': 0.3904941162109375}
store['active_learning_steps'][59]['acquisition']={'indices': [52889, 5440, 360, 33966, 2574], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0227647423744202, 0.9704673290252686, 0.9696877002716064, 0.9688313603401184, 0.9638727903366089]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.285536527633667})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6493033170700073})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4584887623786926})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.430867075920105})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4217025637626648})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4758532643318176})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4297753572463989})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4352043867111206})
store['active_learning_steps'][60]['training']['best_epoch']=5
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9484, 'crossentropy': 0.415252294921875}
store['active_learning_steps'][60]['acquisition']={'indices': [41464, 32573, 5740, 31650, 14825], 'labels': [8, 8, 9, 5, 3], 'scores': [0.9099711775779724, 0.841498076915741, 0.8388579487800598, 0.8360329866409302, 0.8347400426864624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.4074409008026123})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6947041153907776})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5526732802391052})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4832930564880371})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.47515439987182617})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4489566683769226})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5153647661209106})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44230806827545166})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4898403286933899})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4926173686981201})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5339937210083008})
store['active_learning_steps'][61]['training']['best_epoch']=8
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9529, 'crossentropy': 0.4018346923828125}
store['active_learning_steps'][61]['acquisition']={'indices': [42199, 18598, 3694, 14152, 7816], 'labels': [3, 9, -1, 7, 0], 'scores': [1.035945475101471, 0.9992316365242004, 0.9869071245193481, 0.969852864742279, 0.9682536721229553]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.2638866901397705})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6609194874763489})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.43206775188446045})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4672710597515106})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4413440227508545})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49943238496780396})
store['active_learning_steps'][62]['training']['best_epoch']=3
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.948, 'crossentropy': 0.444074169921875}
store['active_learning_steps'][62]['acquisition']={'indices': [1143, 14852, 32445, 32507, 50916], 'labels': [2, 2, 5, 5, 4], 'scores': [0.6949929594993591, 0.6901398301124573, 0.6881017088890076, 0.6828554272651672, 0.6718987226486206]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.2851526737213135})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6858941316604614})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4360758364200592})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44729405641555786})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4716765880584717})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4020729959011078})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.43341559171676636})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4107159376144409})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36453378200531006})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4088440239429474})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.460263729095459})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.44184207916259766})
store['active_learning_steps'][63]['training']['best_epoch']=9
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9565, 'crossentropy': 0.3752315673828125}
store['active_learning_steps'][63]['acquisition']={'indices': [32427, 33150, 22742, 8117, 28844], 'labels': [0, 8, 2, 4, 2], 'scores': [1.0101913809776306, 0.98342365026474, 0.9829651117324829, 0.9521620869636536, 0.9479291439056396]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.292081356048584})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6142276525497437})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.496712327003479})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40246713161468506})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.445570170879364})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42778274416923523})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4280143976211548})
store['active_learning_steps'][64]['training']['best_epoch']=4
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9457, 'crossentropy': 0.39331884765625}
store['active_learning_steps'][64]['acquisition']={'indices': [13969, 1674, 15932, 55739, 52092], 'labels': [3, 9, 7, 5, 7], 'scores': [0.8421921730041504, 0.7929497957229614, 0.7666423320770264, 0.7571538686752319, 0.7448103427886963]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.285761833190918})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6657434701919556})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4849418103694916})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4909721612930298})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39550870656967163})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.46240779757499695})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4506194591522217})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4446870684623718})
store['active_learning_steps'][65]['training']['best_epoch']=5
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9506, 'crossentropy': 0.4065087646484375}
store['active_learning_steps'][65]['acquisition']={'indices': [40184, 4153, 44240, 10256, 57311], 'labels': [3, 2, 3, 2, 5], 'scores': [0.9269983172416687, 0.8638776540756226, 0.8603273630142212, 0.8516284227371216, 0.8397610187530518]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.31923246383667})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.6306918859481812})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4777774214744568})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47770190238952637})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3791924715042114})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4362252652645111})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4544256329536438})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4023057222366333})
store['active_learning_steps'][66]['training']['best_epoch']=5
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9515, 'crossentropy': 0.3791270263671875}
store['active_learning_steps'][66]['acquisition']={'indices': [10260, 39561, 5842, 18003, 15261], 'labels': [3, 2, 1, 2, 3], 'scores': [0.8540246486663818, 0.8176143169403076, 0.816352903842926, 0.8100323677062988, 0.7934185862541199]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.3762577772140503})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.669519305229187})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4965803027153015})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4398782551288605})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.40055906772613525})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40796375274658203})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39305630326271057})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41289836168289185})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.37883123755455017})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4044613242149353})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41404905915260315})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.33850184082984924})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.41999754309654236})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4188270568847656})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48389732837677})
store['active_learning_steps'][67]['training']['best_epoch']=12
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9576, 'crossentropy': 0.357164892578125}
store['active_learning_steps'][67]['acquisition']={'indices': [26376, 8883, 23967, 50734, 5679], 'labels': [1, 2, -1, 5, 3], 'scores': [1.0929445624351501, 1.074768602848053, 1.0554028749465942, 1.041809320449829, 1.03145831823349]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.36997652053833})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7100153565406799})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5041993856430054})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5009503364562988})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39195001125335693})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4030125141143799})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.41002118587493896})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3715153932571411})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37329602241516113})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42978179454803467})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4711550772190094})
store['active_learning_steps'][68]['training']['best_epoch']=8
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9516, 'crossentropy': 0.38716572265625}
store['active_learning_steps'][68]['acquisition']={'indices': [2427, 47595, 39516, 42702, 25310], 'labels': [7, 7, 5, 1, 1], 'scores': [0.9210147857666016, 0.9151977896690369, 0.9108196496963501, 0.9024751782417297, 0.8996128439903259]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.523813247680664})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8381528854370117})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5019655227661133})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.43954384326934814})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3675307333469391})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3881593644618988})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34682196378707886})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3961859941482544})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.39560478925704956})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3603314757347107})
store['active_learning_steps'][69]['training']['best_epoch']=7
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.959, 'crossentropy': 0.3621595458984375}
store['active_learning_steps'][69]['acquisition']={'indices': [6418, 46139, 26266, 9966, 31252], 'labels': [5, 0, 7, 0, 5], 'scores': [0.9837224185466766, 0.9743524193763733, 0.9690065979957581, 0.9475505352020264, 0.9412335753440857]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3698115348815918})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.696600079536438})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4527071714401245})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4493103623390198})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4398759603500366})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.415405809879303})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4016473889350891})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.399172306060791})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4209197163581848})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.349875807762146})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.431207537651062})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3929344415664673})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.40221863985061646})
store['active_learning_steps'][70]['training']['best_epoch']=10
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9589, 'crossentropy': 0.3384375244140625}
store['active_learning_steps'][70]['acquisition']={'indices': [7949, 7984, 30451, 23733, 43745], 'labels': [-1, 4, 8, 5, 8], 'scores': [0.9980324506759644, 0.9953321814537048, 0.9930117130279541, 0.9903164505958557, 0.977417528629303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.2987446784973145})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7340397834777832})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5433014035224915})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4138554036617279})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3888174891471863})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.40286386013031006})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3804154694080353})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.43226924538612366})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.384215772151947})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37052860856056213})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.39292576909065247})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41283994913101196})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38488298654556274})
store['active_learning_steps'][71]['training']['best_epoch']=10
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9534, 'crossentropy': 0.3910756103515625}
store['active_learning_steps'][71]['acquisition']={'indices': [16488, 40022, 42866, 45851, 14210], 'labels': [9, 8, 2, 6, -1], 'scores': [1.0351111888885498, 0.9957879781723022, 0.975692629814148, 0.9743599891662598, 0.9727874994277954]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.3374249935150146})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.7647523880004883})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4376591444015503})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4362804591655731})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33964091539382935})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3427952229976654})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.297041118144989})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.33065423369407654})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33467942476272583})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3584504723548889})
store['active_learning_steps'][72]['training']['best_epoch']=7
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9643, 'crossentropy': 0.3066115478515625}
store['active_learning_steps'][72]['acquisition']={'indices': [13995, 42787, 17832, 13195, 3694], 'labels': [-1, 4, 3, -1, -1], 'scores': [0.9236355423927307, 0.9134615063667297, 0.9125651121139526, 0.8874878883361816, 0.8856818675994873]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.3916983604431152})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.688306450843811})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.46194982528686523})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36447805166244507})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32867515087127686})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2977926731109619})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3023378252983093})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3057959973812103})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3320050835609436})
store['active_learning_steps'][73]['training']['best_epoch']=6
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9623, 'crossentropy': 0.30694140625}
store['active_learning_steps'][73]['acquisition']={'indices': [12305, 13526, 58832, 49656, 31293], 'labels': [9, 9, 3, 9, 8], 'scores': [0.8521072268486023, 0.8516560196876526, 0.8429590463638306, 0.8410772085189819, 0.8394855260848999]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.4427835941314697})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.7200269103050232})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.47966474294662476})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39397162199020386})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39341986179351807})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3975217640399933})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33306604623794556})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39532607793807983})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36965054273605347})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3661273121833801})
store['active_learning_steps'][74]['training']['best_epoch']=7
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9543, 'crossentropy': 0.3588388671875}
store['active_learning_steps'][74]['acquisition']={'indices': [40066, 52590, 14722, 9390, 18193], 'labels': [4, -1, 0, 9, -1], 'scores': [1.0078763365745544, 0.9571018218994141, 0.919736385345459, 0.902982234954834, 0.8980517387390137]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.3646389245986938})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6887322664260864})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4814075827598572})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3853362500667572})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3896748125553131})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34657853841781616})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3318800926208496})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3346300721168518})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3441808223724365})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36411523818969727})
store['active_learning_steps'][75]['training']['best_epoch']=7
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9581, 'crossentropy': 0.353465185546875}
store['active_learning_steps'][75]['acquisition']={'indices': [4564, 52889, 36268, 11616, 5858], 'labels': [-1, -1, 5, 7, -1], 'scores': [0.9343978762626648, 0.9138622283935547, 0.9011871516704559, 0.8837152123451233, 0.8807582855224609]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.3132542371749878})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.6543499827384949})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.45490792393684387})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3655986189842224})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30850327014923096})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33794599771499634})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3361603915691376})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28285759687423706})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28473377227783203})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3125898838043213})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29181480407714844})
store['active_learning_steps'][76]['training']['best_epoch']=8
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9629, 'crossentropy': 0.307009423828125}
store['active_learning_steps'][76]['acquisition']={'indices': [31046, 34847, 20169, 17079, 20903], 'labels': [6, 0, 4, 6, 3], 'scores': [0.943732500076294, 0.9407865405082703, 0.9398994445800781, 0.9274730086326599, 0.9256742596626282]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.4196369647979736})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.8291300535202026})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.491179496049881})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.42054763436317444})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41487571597099304})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38350293040275574})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3413722813129425})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3739379048347473})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3365861773490906})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.363714337348938})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3334748446941376})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33991697430610657})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37898576259613037})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33660244941711426})
store['active_learning_steps'][77]['training']['best_epoch']=11
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9601, 'crossentropy': 0.3358465087890625}
store['active_learning_steps'][77]['acquisition']={'indices': [3580, 45972, 5298, 623, 34665], 'labels': [5, 2, 0, 6, 9], 'scores': [1.0446289777755737, 1.0372576713562012, 1.0025781393051147, 1.0020508766174316, 1.0000863671302795]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.3041216135025024})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.6642988324165344})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.43323415517807007})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.344402015209198})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.3135118782520294})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.32491323351860046})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29341402649879456})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2949136793613434})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3207307755947113})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29371756315231323})
store['active_learning_steps'][78]['training']['best_epoch']=7
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9605, 'crossentropy': 0.3046414306640625}
store['active_learning_steps'][78]['acquisition']={'indices': [43648, 8214, 59836, 57507, 52889], 'labels': [5, 7, 1, 0, -1], 'scores': [0.886526346206665, 0.8638635277748108, 0.8402027487754822, 0.8363336324691772, 0.8290475606918335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.4423036575317383})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7166810035705566})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4824255704879761})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3910202085971832})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35137656331062317})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3544483780860901})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.346932053565979})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32955682277679443})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3273085653781891})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32979661226272583})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29877495765686035})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3468855023384094})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.308948814868927})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3383048176765442})
store['active_learning_steps'][79]['training']['best_epoch']=11
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.3067692626953125}
store['active_learning_steps'][79]['acquisition']={'indices': [13998, 4955, 59286, 32747, 4850], 'labels': [9, 2, 8, 8, 3], 'scores': [1.0525505542755127, 1.0505448579788208, 1.0195582509040833, 1.0018289685249329, 0.9714861512184143]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.4139420986175537})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.704421877861023})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.5111979842185974})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.38000571727752686})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3081749677658081})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32766133546829224})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3113870620727539})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32624351978302})
store['active_learning_steps'][80]['training']['best_epoch']=5
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9578, 'crossentropy': 0.3702491943359375}
store['active_learning_steps'][80]['acquisition']={'indices': [47626, 37450, 38920, 4185, 45944], 'labels': [-1, 4, 7, 2, 9], 'scores': [0.7962921857833862, 0.7817215919494629, 0.7717546224594116, 0.7665930986404419, 0.7584917545318604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.402529239654541})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6937907934188843})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4842923879623413})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3705495595932007})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3546385169029236})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3312438130378723})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3288029432296753})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31533926725387573})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3039311170578003})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2946019768714905})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33020085096359253})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.35403791069984436})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3823397159576416})
store['active_learning_steps'][81]['training']['best_epoch']=10
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.2929046875}
store['active_learning_steps'][81]['acquisition']={'indices': [52590, 49910, 36761, 31512, 29255], 'labels': [-1, 6, -1, 2, -1], 'scores': [1.089957594871521, 1.0604096055030823, 0.9897736310958862, 0.9425083994865417, 0.9348863363265991]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.521148681640625})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7519030570983887})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4635365903377533})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3536868095397949})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3193974494934082})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3140718340873718})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30563297867774963})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30657610297203064})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3113460838794708})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3157895505428314})
store['active_learning_steps'][82]['training']['best_epoch']=7
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.3015234375}
store['active_learning_steps'][82]['acquisition']={'indices': [29110, 29376, 46975, 43112, 22728], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9784687757492065, 0.9479681253433228, 0.9328789710998535, 0.9164620637893677, 0.9030057787895203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.4186935424804688})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.7893104553222656})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4912223815917969})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3652440905570984})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3665195405483246})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3223540782928467})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3496781587600708})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3061254322528839})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35006090998649597})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.34582746028900146})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3175017535686493})
store['active_learning_steps'][83]['training']['best_epoch']=8
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9611, 'crossentropy': 0.321212255859375}
store['active_learning_steps'][83]['acquisition']={'indices': [13774, 54950, 28536, 51180, 29672], 'labels': [2, 8, 3, 7, 9], 'scores': [0.9292309284210205, 0.9239525198936462, 0.8989260196685791, 0.890536904335022, 0.8904834389686584]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.4450167417526245})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6977798342704773})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.4517035484313965})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.4006499946117401})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3703537881374359})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3362070322036743})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2998085618019104})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3030955195426941})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32021957635879517})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3145185112953186})
store['active_learning_steps'][84]['training']['best_epoch']=7
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.31168369140625}
store['active_learning_steps'][84]['acquisition']={'indices': [32668, 7949, 44927, 37538, 38912], 'labels': [9, -1, 7, 9, -1], 'scores': [0.9749616384506226, 0.9447627663612366, 0.9215638637542725, 0.9089240431785583, 0.9054833650588989]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.3268380165100098})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6978111267089844})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.46129167079925537})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36439502239227295})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31365853548049927})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2865625321865082})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28147822618484497})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26682108640670776})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2619988024234772})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.26592788100242615})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29238778352737427})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24263018369674683})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2987796664237976})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.29114800691604614})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29897040128707886})
store['active_learning_steps'][85]['training']['best_epoch']=12
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9699, 'crossentropy': 0.2719778076171875}
store['active_learning_steps'][85]['acquisition']={'indices': [47626, 13156, 50736, 59081, 4564], 'labels': [-1, 2, -1, -1, -1], 'scores': [1.030672013759613, 1.0164366960525513, 1.0076895952224731, 0.9679074883460999, 0.9650144577026367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.3610494136810303})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.7186369895935059})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4564451575279236})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35736531019210815})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32264479994773865})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3089345693588257})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3248863220214844})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.288746178150177})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2857927680015564})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2792191505432129})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3173789381980896})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28860339522361755})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2937740981578827})
store['active_learning_steps'][86]['training']['best_epoch']=10
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.2852430419921875}
store['active_learning_steps'][86]['acquisition']={'indices': [41094, 50840, 38397, 2600, 26405], 'labels': [-1, 2, 8, 9, 9], 'scores': [0.9448881149291992, 0.9411300420761108, 0.9409226775169373, 0.9359228014945984, 0.9334784746170044]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.3402445316314697})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7250211238861084})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4844939112663269})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37248295545578003})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.40220415592193604})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.32845813035964966})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29763931035995483})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28409042954444885})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3188019394874573})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34844571352005005})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30507171154022217})
store['active_learning_steps'][87]['training']['best_epoch']=8
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9624, 'crossentropy': 0.3027113525390625}
store['active_learning_steps'][87]['acquisition']={'indices': [41426, 1682, 262, 24462, 42472], 'labels': [4, 0, 2, 2, 2], 'scores': [0.9788419604301453, 0.9523032903671265, 0.9512553811073303, 0.9122753739356995, 0.9066380262374878]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.4992399215698242})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.7278687953948975})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.494868665933609})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.43285006284713745})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35936421155929565})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3708449602127075})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3325769901275635})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.33911916613578796})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3252595067024231})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3422248363494873})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.351637601852417})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3428228795528412})
store['active_learning_steps'][88]['training']['best_epoch']=9
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.3171839599609375}
store['active_learning_steps'][88]['acquisition']={'indices': [48102, 39877, 24006, 53196, 19597], 'labels': [7, 7, 9, 9, 9], 'scores': [0.9985527396202087, 0.9138932824134827, 0.8917107582092285, 0.8869225978851318, 0.8826299905776978]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.2930576801300049})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.7246813774108887})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4489666819572449})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3801348805427551})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3327314257621765})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2973824739456177})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3507605791091919})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33569324016571045})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.31860095262527466})
store['active_learning_steps'][89]['training']['best_epoch']=6
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.967, 'crossentropy': 0.330495263671875}
store['active_learning_steps'][89]['acquisition']={'indices': [49616, 40046, 54210, 38974, 7308], 'labels': [7, 7, 1, 1, 8], 'scores': [0.9404467940330505, 0.8995766639709473, 0.8903714418411255, 0.8455435633659363, 0.8431826233863831]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.4738531112670898})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7507246732711792})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5256063938140869})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.36637425422668457})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3338027596473694})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.34563982486724854})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31211909651756287})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31052690744400024})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30982711911201477})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3077971339225769})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3184663951396942})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2949219048023224})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3354455232620239})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32222694158554077})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.34246641397476196})
store['active_learning_steps'][90]['training']['best_epoch']=12
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.965, 'crossentropy': 0.305302490234375}
store['active_learning_steps'][90]['acquisition']={'indices': [52590, 46975, 16997, 27176, 55244], 'labels': [-1, -1, 0, 5, 7], 'scores': [1.0088287591934204, 1.0050504207611084, 0.9985281825065613, 0.997494637966156, 0.9921581745147705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.4656703472137451})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6657209396362305})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.45050451159477234})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34583574533462524})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3788817524909973})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34450751543045044})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29406630992889404})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28097301721572876})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2766778767108917})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.264473021030426})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29419976472854614})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.28766724467277527})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29386231303215027})
store['active_learning_steps'][91]['training']['best_epoch']=10
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9739, 'crossentropy': 0.2748060546875}
store['active_learning_steps'][91]['acquisition']={'indices': [10181, 46975, 57322, 39645, 7949], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0396905541419983, 1.0207396745681763, 0.9902864694595337, 0.9890486001968384, 0.9884458780288696]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.5360374450683594})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.843506932258606})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4993519186973572})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4035654067993164})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37154680490493774})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2900717854499817})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35692018270492554})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30065834522247314})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.291947603225708})
store['active_learning_steps'][92]['training']['best_epoch']=6
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9655, 'crossentropy': 0.311264453125}
store['active_learning_steps'][92]['acquisition']={'indices': [29376, 54401, 53654, 6574, 38223], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.87291020154953, 0.8676499128341675, 0.8585212230682373, 0.8442957401275635, 0.8438959717750549]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.3544561862945557})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.734784722328186})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5098342895507812})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36716556549072266})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3609544038772583})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.339841365814209})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30924296379089355})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3198637366294861})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2892787456512451})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.27918297052383423})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28209537267684937})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3006647229194641})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.29821306467056274})
store['active_learning_steps'][93]['training']['best_epoch']=10
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.3003983642578125}
store['active_learning_steps'][93]['acquisition']={'indices': [41714, 2845, 45424, 31672, 59321], 'labels': [4, 8, 4, 6, 4], 'scores': [1.0371896028518677, 1.0073782205581665, 1.0003220438957214, 0.9538112282752991, 0.9508031010627747]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.3807060718536377})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.7718390226364136})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5493564605712891})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41593337059020996})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3588726222515106})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3513637185096741})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3093337416648865})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32721197605133057})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28723257780075073})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25649046897888184})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.27203428745269775})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3496705889701843})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3296794891357422})
store['active_learning_steps'][94]['training']['best_epoch']=10
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.28377724609375}
store['active_learning_steps'][94]['acquisition']={'indices': [42438, 52590, 45954, 635, 6347], 'labels': [9, -1, 8, 5, 3], 'scores': [0.9754484295845032, 0.9454763531684875, 0.9433602094650269, 0.9366937875747681, 0.9354763031005859]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.3305813074111938})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6799519658088684})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.500527024269104})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.4018782079219818})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3633838891983032})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2641063928604126})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27765798568725586})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2755310833454132})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2632531523704529})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.24807286262512207})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2718151807785034})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.24388529360294342})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.25315579771995544})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.26524391770362854})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.25063174962997437})
store['active_learning_steps'][95]['training']['best_epoch']=12
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9707, 'crossentropy': 0.28469443359375}
store['active_learning_steps'][95]['acquisition']={'indices': [10756, 2782, 31587, 46995, 45189], 'labels': [3, -1, -1, -1, -1], 'scores': [1.0064542293548584, 0.9909478425979614, 0.9817185401916504, 0.9812924861907959, 0.9776052832603455]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.3747638463974})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.7130571603775024})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3877468705177307})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.41732460260391235})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2954860329627991})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.30438733100891113})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3148432970046997})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.2444034069776535})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31560230255126953})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28759127855300903})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2859828770160675})
store['active_learning_steps'][96]['training']['best_epoch']=8
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.284186328125}
store['active_learning_steps'][96]['acquisition']={'indices': [49573, 11071, 3694, 34353, 42775], 'labels': [2, -1, -1, -1, -1], 'scores': [0.9184355735778809, 0.9127546548843384, 0.8996158242225647, 0.8981753587722778, 0.8977307677268982]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.4112915992736816})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.750924825668335})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5019891262054443})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36868375539779663})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36087721586227417})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32372257113456726})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30647706985473633})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3135721683502197})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2876942455768585})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3045569062232971})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2745213508605957})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3110802173614502})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2700766623020172})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28416314721107483})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28916236758232117})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2950226366519928})
store['active_learning_steps'][97]['training']['best_epoch']=13
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9667, 'crossentropy': 0.301964404296875}
store['active_learning_steps'][97]['acquisition']={'indices': [45171, 6130, 46017, 54556, 7886], 'labels': [-1, 7, 0, 2, 9], 'scores': [1.0236653685569763, 1.0169147849082947, 0.9975723028182983, 0.9862295985221863, 0.9727887511253357]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.4411346912384033})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7868545055389404})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.44516563415527344})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3617119789123535})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3403109908103943})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31499606370925903})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2894819974899292})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29849711060523987})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2882000803947449})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3009452223777771})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28807079792022705})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2907686233520508})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2856016755104065})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28114187717437744})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3187503218650818})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27324748039245605})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30978113412857056})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.29588377475738525})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.3004831373691559})
store['active_learning_steps'][98]['training']['best_epoch']=16
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9665, 'crossentropy': 0.3080744384765625}
store['active_learning_steps'][98]['acquisition']={'indices': [20942, 52800, 29440, 4156, 803], 'labels': [3, 9, 7, 3, -1], 'scores': [1.0647140145301819, 1.0464025735855103, 1.031978964805603, 1.031365156173706, 1.027726948261261]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.609170913696289})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.843273401260376})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5265570878982544})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.39114058017730713})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.34288060665130615})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3178442418575287})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.28531336784362793})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9814453125, 'crossentropy': 0.26959657669067383})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24947136640548706})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2704852223396301})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2642216682434082})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.24457542598247528})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3190901279449463})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2277604043483734})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.24308115243911743})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.256176620721817})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2904486656188965})
store['active_learning_steps'][99]['training']['best_epoch']=14
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.2691946044921875}
store['active_learning_steps'][99]['acquisition']={'indices': [41933, 52590, 22139, 29255, 32928], 'labels': [5, -1, 2, -1, -1], 'scores': [1.080069124698639, 1.0413722395896912, 1.0112869143486023, 1.004233717918396, 1.0018556714057922]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.422598123550415})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.7480024099349976})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.5139338970184326})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3356637954711914})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34135037660598755})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27999162673950195})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2755146324634552})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2718396484851837})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25874343514442444})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25012633204460144})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25364312529563904})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2949446737766266})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2684382200241089})
store['active_learning_steps'][100]['training']['best_epoch']=10
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.265922412109375}
