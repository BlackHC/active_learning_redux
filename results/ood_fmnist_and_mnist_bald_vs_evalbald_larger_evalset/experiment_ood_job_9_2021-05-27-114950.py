store = {}
store['timestamp']=1622112590
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=9']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=9
store['worker_id']=9
store['num_workers']=80
store['config']={'seed': 1243, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.367323398590088})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.7427845001220703})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.125979423522949})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.0779480934143066})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.377722978591919})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.156877040863037})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.025387763977051})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6177, 'crossentropy': 3.21715859375}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 49418], ['ood', 42354], ['ood', 49896], ['ood', 27319], ['ood', 35031]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.5916399037928892, 2.7750979785408862, 3.641748221226833, 4.14630751550503, 4.383529393899585]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.7763643264770508})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.5588173866271973})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.8377325534820557})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.878312110900879})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.847546339035034})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.1054012775421143})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.4288201332092285})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5996, 'crossentropy': 3.001508203125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 2312], ['ood', 51786], ['ood', 39427], ['id', 19888], ['id', 3545]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1148906596794372, 2.046489146646193, 2.8672428829392143, 3.466059677558386, 3.8721798117856547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.6267341375350952})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.5944862365722656})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.4478087425231934})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.81919264793396})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.8646504878997803})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.8612723350524902})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6197, 'crossentropy': 2.6824505859375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 56561], ['id', 25897], ['id', 8485], ['id', 11531], ['id', 50930]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.9160493852610478, 1.7210360045819204, 2.361242180429871, 2.9109132093586485, 3.3241076240701943]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.4451853036880493})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.7429263591766357})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.226935625076294})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.3689448833465576})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.6381006240844727})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.621, 'crossentropy': 2.0700865234375}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 39750], ['id', 12692], ['ood', 20250], ['id', 35305], ['id', 54785]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8406724845643014, 1.5754638620242498, 2.259197749797023, 2.789156848651513, 3.242809634351861]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.4412951469421387})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.9186915159225464})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.107712984085083})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.4041082859039307})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6149, 'crossentropy': 1.45990947265625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 26676], ['id', 4915], ['id', 43193], ['id', 31587], ['id', 18729]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5969948119023756, 1.0978965108750827, 1.5415732236683333, 1.952042663014689, 2.3293265585867147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.5113080739974976})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.9243278503417969})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.240231990814209})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.4101767539978027})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.0874063968658447})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.7397115230560303})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.8380842208862305})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.7835559844970703})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.3272390365600586})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.1608078479766846})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.0818963050842285})
store['active_learning_steps'][5]['training']['best_epoch']=8
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6185, 'crossentropy': 2.83950625}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 40224], ['id', 59111], ['id', 18003], ['id', 51231], ['id', 39951]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9796035274460193, 1.9101210778116182, 2.6460778697269944, 3.25334580183144, 3.7239319510318367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2996227741241455})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.821051836013794})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.9672094583511353})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.171780586242676})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6284, 'crossentropy': 1.36113515625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 20332], ['id', 21487], ['id', 16361], ['id', 37251], ['ood', 29640]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5458370832772053, 1.0556676696350462, 1.5154455893936989, 1.892752510955515, 2.2416005902507568]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.3906787633895874})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.504030704498291})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.830474853515625})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.0304903984069824})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.0296437740325928})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.2828197479248047})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.575613260269165})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6417, 'crossentropy': 2.1073681640625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 27090], ['id', 59771], ['id', 46576], ['id', 40549], ['ood', 56709]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.941124343101329, 1.7505835837394628, 2.4567331488890036, 3.0388268664597264, 3.4767910690421626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.368226408958435})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4882876873016357})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.6913485527038574})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.870070219039917})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.199913501739502})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.316830635070801})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6403, 'crossentropy': 1.72591953125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 56635], ['id', 28663], ['id', 17345], ['id', 57808], ['id', 13598]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.788874793421813, 1.5125200291317396, 2.1601224204089116, 2.722075813430779, 3.1684138090886336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.2989418506622314})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.491108775138855})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.7059807777404785})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.0697760581970215})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.9114265441894531})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.430093288421631})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.4846324920654297})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.2345666885375977})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.51102614402771})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.6417622566223145})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.5422651767730713})
store['active_learning_steps'][9]['training']['best_epoch']=8
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6129, 'crossentropy': 2.4771259765625}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 19842], ['id', 24172], ['id', 23978], ['id', 17698], ['id', 14065]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.0054742799879612, 1.9294242125653485, 2.7054254551666794, 3.328058646457973, 3.745543707200685]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.3436775207519531})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.4733502864837646})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.8351521492004395})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.055617094039917})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.2169764041900635})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.3883914947509766})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5939, 'crossentropy': 1.912521484375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 8628], ['id', 50873], ['id', 34994], ['id', 7456], ['id', 56860]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7209185416314972, 1.3936320632739845, 1.9915486579836852, 2.50782079143283, 2.943151982467027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.3940389156341553})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.463782787322998})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.7497138977050781})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.063153028488159})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.3176639080047607})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.345663070678711})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.1749939918518066})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.5142757892608643})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.5440502166748047})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.814377784729004})
store['active_learning_steps'][11]['training']['best_epoch']=7
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6089, 'crossentropy': 2.5959421875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 47656], ['id', 6080], ['id', 31345], ['id', 7671], ['id', 20348]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9426661384336461, 1.7642773672178569, 2.478906684085361, 3.0784963380429655, 3.5498376499800823]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.494746208190918})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.3747823238372803})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.5933640003204346})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.7588779926300049})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.919257640838623})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.9501020908355713})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.9016801118850708})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.4216601848602295})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.0832674503326416})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6165, 'crossentropy': 2.0381888671875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 49919], ['id', 40304], ['id', 1120], ['id', 58220], ['id', 45967]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8554132453006846, 1.6252897348075441, 2.3006290642125933, 2.887260477796646, 3.360921204604187]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.3491970300674438})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3057546615600586})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.4499460458755493})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.7712430953979492})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.7172245979309082})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.7320005893707275})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.9598702192306519})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.8149690628051758})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.8967013359069824})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.092824935913086})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.078237295150757})
store['active_learning_steps'][13]['training']['best_epoch']=8
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.649, 'crossentropy': 2.08419375}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 29532], ['id', 29955], ['id', 52321], ['ood', 5790], ['id', 47104]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9185711612293224, 1.7601795558743554, 2.508062395961125, 3.1160805297069185, 3.556711933726943]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.529296875, 'crossentropy': 1.475369930267334})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.2280595302581787})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3024309873580933})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.484368085861206})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.5543094873428345})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.6789486408233643})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.014920949935913})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.7264750003814697})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6519, 'crossentropy': 1.681428515625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 34549], ['id', 8919], ['id', 19837], ['id', 24964], ['ood', 19689]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9086105299479588, 1.751221398496694, 2.4728174430912624, 3.0645197844745073, 3.5097522362931413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.330482840538025})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2000584602355957})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2690696716308594})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.4116103649139404})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.4601550102233887})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.7481811046600342})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.6397773027420044})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.7593779563903809})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.798824667930603})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.647, 'crossentropy': 1.8146833984375}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 20867], ['id', 1087], ['id', 26636], ['id', 3879], ['id', 39814]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9475316049271676, 1.7804333595144497, 2.5346055124355047, 3.165989819699747, 3.639191542439095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.358668565750122})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1517348289489746})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3134541511535645})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3792774677276611})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.439724326133728})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.5246756076812744})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6548, 'crossentropy': 1.335370703125}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 32171], ['id', 30178], ['id', 15800], ['id', 48685], ['id', 26462]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7099035048202342, 1.344152453636923, 1.9254324682386148, 2.4422265603789253, 2.8764724114592717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5537109375, 'crossentropy': 1.4308407306671143})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.338376522064209})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.413332462310791})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.5874054431915283})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.7419102191925049})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.8505494594573975})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6474, 'crossentropy': 1.43879892578125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 45096], ['id', 27260], ['id', 50385], ['ood', 25662], ['id', 5355]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7916964678346754, 1.5030719240213606, 2.0960604871485504, 2.6117206266010786, 3.0362189341578034]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.5380859375, 'crossentropy': 1.406970739364624})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1554466485977173})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2640087604522705})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.398923397064209})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.5639431476593018})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.5972073078155518})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.5671756267547607})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.7058981657028198})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.837502360343933})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6504, 'crossentropy': 1.7762306640625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 41355], ['id', 6935], ['id', 55160], ['id', 26174], ['id', 24079]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9598806953592693, 1.7848440123107752, 2.5001105425629966, 3.096408535738866, 3.533624151971834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5400390625, 'crossentropy': 1.4146146774291992})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1300922632217407})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3314310312271118})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3815093040466309})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3753331899642944})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.5378395318984985})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.781213402748108})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6484, 'crossentropy': 1.49510166015625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 27863], ['id', 22547], ['id', 12078], ['id', 38613], ['id', 43793]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.805560590511907, 1.5630211278795936, 2.1815888705324236, 2.725628746439283, 3.177654466249381]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5576171875, 'crossentropy': 1.445698618888855})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1964709758758545})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2666476964950562})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3592166900634766})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.5697181224822998})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.5548852682113647})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.7477377653121948})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.8506500720977783})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.667384386062622})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.673117756843567})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.8821444511413574})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.2240724563598633})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.992242693901062})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.0239381790161133})
store['active_learning_steps'][20]['training']['best_epoch']=11
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6458, 'crossentropy': 1.9591126953125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 34920], ['id', 46563], ['id', 40187], ['id', 9232], ['id', 16858]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0007602819602457, 1.9112855009208705, 2.6809749960619857, 3.3008395583048706, 3.7437230934479695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.4943124055862427})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.2593662738800049})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.3359516859054565})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2858185768127441})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.36716628074646})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.5004397630691528})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.543368935585022})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.5905619859695435})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.6625378131866455})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.6188100576400757})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.6605515480041504})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.7668581008911133})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.7974227666854858})
store['active_learning_steps'][21]['training']['best_epoch']=10
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.652, 'crossentropy': 1.8013220703125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 12195], ['id', 3913], ['id', 7532], ['id', 44841], ['id', 17463]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9798046688533626, 1.8615336015524817, 2.622279709674606, 3.2659171490304724, 3.708119919158791]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 1.46608567237854})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.3315649032592773})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2606050968170166})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3741116523742676})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.4853113889694214})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.6405565738677979})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6352, 'crossentropy': 1.3595595703125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 33781], ['id', 28733], ['id', 37367], ['id', 27747], ['id', 22224]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6332637383466613, 1.2165328190078197, 1.7555702387077616, 2.237132709977007, 2.661878589360793]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 1.433837890625})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.1944465637207031})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1620540618896484})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1848218441009521})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.2627264261245728})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.5279691219329834})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.5097121000289917})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.679175853729248})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.655, 'crossentropy': 1.4098310546875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 7460], ['id', 23444], ['id', 31065], ['id', 25420], ['id', 587]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9175087261052952, 1.658899978391175, 2.280739505504198, 2.8243411958283504, 3.244150772112844]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.5152442455291748})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.246166706085205})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2840023040771484})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.318374514579773})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4604249000549316})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.5631130933761597})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.698228120803833})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.7285830974578857})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.8658398389816284})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.7013639211654663})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.9836440086364746})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.9203736782073975})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.060666561126709})
store['active_learning_steps'][24]['training']['best_epoch']=10
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6502, 'crossentropy': 1.98345703125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 1479], ['id', 3919], ['id', 36120], ['id', 16490], ['id', 38100]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9911498168493234, 1.8435955730922249, 2.5733420076563505, 3.1918593207698116, 3.6467259269300296]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5556640625, 'crossentropy': 1.5530385971069336})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.296823501586914})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.200338363647461})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2686114311218262})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3421351909637451})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.4481871128082275})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6434, 'crossentropy': 1.24040693359375}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 59671], ['id', 50403], ['ood', 48608], ['id', 6000], ['id', 45484]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6030991336120715, 1.1432935039111092, 1.6550618727917321, 2.126386087303187, 2.5438197732270647]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.5317814350128174})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.2666707038879395})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1950795650482178})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1997565031051636})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3527014255523682})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.4405159950256348})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.492215633392334})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.4960143566131592})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.7890243530273438})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.7011293172836304})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6409, 'crossentropy': 1.6392224609375}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 54813], ['id', 20157], ['id', 42826], ['id', 59860], ['id', 34122]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.8850913943152654, 1.6557808867750206, 2.3332879971584903, 2.916526584250617, 3.38218981390129]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.4677118062973022})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1980640888214111})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.1366480588912964})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.20823073387146})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.2967123985290527})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4826369285583496})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.5488989353179932})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.691262125968933})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.7004103660583496})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.649548888206482})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.7795803546905518})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.7927448749542236})
store['active_learning_steps'][27]['training']['best_epoch']=9
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6517, 'crossentropy': 1.9521857421875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 58420], ['id', 27592], ['id', 49995], ['id', 8506], ['id', 36323]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9695796869262912, 1.828809363777618, 2.5331057723441974, 3.1137003299510484, 3.5423987655479907]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.55078125, 'crossentropy': 1.584921956062317})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.22850501537323})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.311253547668457})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2997184991836548})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3005353212356567})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.4711874723434448})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.5439984798431396})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.5557940006256104})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6383, 'crossentropy': 1.40978056640625}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 55037], ['id', 47904], ['ood', 49430], ['id', 33035], ['id', 2434]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7032150684639813, 1.3798010838071524, 2.000254467874063, 2.519397163947988, 2.9654046794126288]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 1.5735697746276855})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.1929512023925781})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1391627788543701})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1754446029663086})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3403112888336182})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.4136302471160889})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.4789988994598389})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6564, 'crossentropy': 1.289341015625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 32065], ['id', 43863], ['id', 47659], ['id', 2910], ['id', 11036]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6586790995447644, 1.2776393885985735, 1.823940610730837, 2.324333790058968, 2.756111991856624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5380859375, 'crossentropy': 1.560835361480713})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2283101081848145})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1568703651428223})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1984745264053345})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3494720458984375})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.4318995475769043})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6668, 'crossentropy': 1.200480859375}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 25798], ['ood', 31020], ['id', 58746], ['ood', 10319], ['ood', 38716]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5384635459812799, 1.0363545347908358, 1.5065814620456903, 1.9571784571574167, 2.355588163534313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5322265625, 'crossentropy': 1.6135239601135254})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.251237154006958})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1556059122085571})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2420654296875})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3060455322265625})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.3274595737457275})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.4510152339935303})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.4738329648971558})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.509784460067749})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.6018431186676025})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.59286367893219})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.6124931573867798})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.7402293682098389})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.5641047954559326})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.6356630325317383})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.7026112079620361})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.7994935512542725})
store['active_learning_steps'][31]['training']['best_epoch']=14
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6757, 'crossentropy': 1.7777900390625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 4809], ['id', 45568], ['id', 5937], ['id', 59953], ['id', 45176]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9920497159793149, 1.887294014555148, 2.6416983134585346, 3.262508457685877, 3.7237457458443988]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.525390625, 'crossentropy': 1.527843713760376})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2389451265335083})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.183868646621704})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2032554149627686})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.2595455646514893})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2922325134277344})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.3974483013153076})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.4712517261505127})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.5786831378936768})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6756, 'crossentropy': 1.4149021484375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 30476], ['id', 7475], ['id', 5893], ['id', 1961], ['id', 13237]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7217579598132144, 1.4037550053178176, 2.037393396104286, 2.5673426002060316, 3.0173354181458896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.50390625, 'crossentropy': 1.5265707969665527})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1700598001480103})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1414926052093506})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1382503509521484})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1877071857452393})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3248717784881592})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.3274521827697754})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.4069252014160156})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6895, 'crossentropy': 1.22556611328125}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 55098], ['id', 38974], ['id', 5413], ['id', 57132], ['id', 53488]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7242680367899443, 1.4097276693982144, 2.0218592458328253, 2.5564160666295646, 3.015076701736172]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5185546875, 'crossentropy': 1.5384490489959717})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2238364219665527})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.101569414138794})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.080712080001831})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2663207054138184})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.3714849948883057})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6818, 'crossentropy': 1.1368994140625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 42536], ['id', 43543], ['id', 11274], ['id', 12151], ['id', 8387]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5718596809857961, 1.0981728524212384, 1.5425650816204266, 1.9457563005238132, 2.3210538635403797]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.498046875, 'crossentropy': 1.5727128982543945})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2307040691375732})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1875991821289062})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2771083116531372})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.317563772201538})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.633, 'crossentropy': 1.26354677734375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 18584], ['id', 58560], ['id', 4436], ['ood', 59701], ['id', 36843]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.41744468481315944, 0.769736665769365, 1.1001723368843717, 1.4108617591890793, 1.6955045677494098]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.464531421661377})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.207925796508789})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0999634265899658})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1853824853897095})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.2153244018554688})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.2642130851745605})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.2548305988311768})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.2527387142181396})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.4150233268737793})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.4832054376602173})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.45064115524292})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7002, 'crossentropy': 1.33159599609375}
